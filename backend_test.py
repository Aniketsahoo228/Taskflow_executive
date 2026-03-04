import requests
import sys
import json
from datetime import datetime, timedelta

class TaskFlowAPITester:
    def __init__(self, base_url="https://task-manager-pro-39.preview.emergentagent.com/api"):
        self.base_url = base_url
        self.token = None
        self.user_id = None
        self.tests_run = 0
        self.tests_passed = 0
        self.test_user_email = f"test_user_{datetime.now().strftime('%H%M%S')}@test.com"
        self.test_user_password = "TestPass123!"
        self.test_user_name = "Test User"
        self.created_task_id = None

    def run_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        test_headers = {'Content-Type': 'application/json'}
        
        if self.token:
            test_headers['Authorization'] = f'Bearer {self.token}'
        
        if headers:
            test_headers.update(headers)

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=test_headers, params=data)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=test_headers)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=test_headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=test_headers)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    print(f"   Response: {json.dumps(response_data, indent=2)[:200]}...")
                    return True, response_data
                except:
                    return True, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"   Error: {error_data}")
                except:
                    print(f"   Error: {response.text}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_register(self):
        """Test user registration"""
        success, response = self.run_test(
            "User Registration",
            "POST",
            "auth/register",
            200,
            data={
                "email": self.test_user_email,
                "password": self.test_user_password,
                "name": self.test_user_name
            }
        )
        if success and 'access_token' in response:
            self.token = response['access_token']
            self.user_id = response['user']['id']
            print(f"   Token obtained: {self.token[:20]}...")
            return True
        return False

    def test_login(self):
        """Test user login"""
        success, response = self.run_test(
            "User Login",
            "POST",
            "auth/login",
            200,
            data={
                "email": self.test_user_email,
                "password": self.test_user_password
            }
        )
        if success and 'access_token' in response:
            self.token = response['access_token']
            self.user_id = response['user']['id']
            print(f"   Login successful for user: {response['user']['name']}")
            return True
        return False

    def test_create_task(self):
        """Test task creation"""
        task_data = {
            "title": "Test Task",
            "description": "This is a test task description",
            "status": "pending",
            "priority": "high",
            "due_date": (datetime.now() + timedelta(days=7)).isoformat(),
            "categories": ["work", "urgent"]
        }
        
        success, response = self.run_test(
            "Create Task",
            "POST",
            "tasks",
            200,
            data=task_data
        )
        if success and 'id' in response:
            self.created_task_id = response['id']
            print(f"   Task created with ID: {self.created_task_id}")
            return True
        return False

    def test_get_tasks(self):
        """Test getting all tasks"""
        success, response = self.run_test(
            "Get All Tasks",
            "GET",
            "tasks",
            200
        )
        if success and isinstance(response, list):
            print(f"   Found {len(response)} tasks")
            return True
        return False

    def test_get_single_task(self):
        """Test getting a single task"""
        if not self.created_task_id:
            print("❌ No task ID available for single task test")
            return False
            
        success, response = self.run_test(
            "Get Single Task",
            "GET",
            f"tasks/{self.created_task_id}",
            200
        )
        if success and 'id' in response:
            print(f"   Retrieved task: {response['title']}")
            return True
        return False

    def test_update_task(self):
        """Test updating a task"""
        if not self.created_task_id:
            print("❌ No task ID available for update test")
            return False
            
        update_data = {
            "title": "Updated Test Task",
            "status": "completed",
            "priority": "medium"
        }
        
        success, response = self.run_test(
            "Update Task",
            "PUT",
            f"tasks/{self.created_task_id}",
            200,
            data=update_data
        )
        if success and response.get('title') == "Updated Test Task":
            print(f"   Task updated successfully")
            return True
        return False

    def test_filter_tasks_by_status(self):
        """Test filtering tasks by status"""
        success, response = self.run_test(
            "Filter Tasks by Status",
            "GET",
            "tasks",
            200,
            data={"status": "completed"}
        )
        if success:
            print(f"   Found {len(response)} completed tasks")
            return True
        return False

    def test_filter_tasks_by_priority(self):
        """Test filtering tasks by priority"""
        success, response = self.run_test(
            "Filter Tasks by Priority",
            "GET",
            "tasks",
            200,
            data={"priority": "high"}
        )
        if success:
            print(f"   Found {len(response)} high priority tasks")
            return True
        return False

    def test_search_tasks(self):
        """Test searching tasks"""
        success, response = self.run_test(
            "Search Tasks",
            "GET",
            "tasks",
            200,
            data={"search": "Test"}
        )
        if success:
            print(f"   Found {len(response)} tasks matching 'Test'")
            return True
        return False

    def test_delete_task(self):
        """Test deleting a task"""
        if not self.created_task_id:
            print("❌ No task ID available for delete test")
            return False
            
        success, response = self.run_test(
            "Delete Task",
            "DELETE",
            f"tasks/{self.created_task_id}",
            200
        )
        if success:
            print(f"   Task deleted successfully")
            return True
        return False

    def test_unauthorized_access(self):
        """Test accessing protected endpoints without token"""
        original_token = self.token
        self.token = None
        
        success, response = self.run_test(
            "Unauthorized Access Test",
            "GET",
            "tasks",
            401  # Should return 401 Unauthorized
        )
        
        self.token = original_token
        return success

def main():
    print("🚀 Starting TaskFlow API Tests")
    print("=" * 50)
    
    tester = TaskFlowAPITester()
    
    # Test sequence
    tests = [
        ("User Registration", tester.test_register),
        ("User Login", tester.test_login),
        ("Create Task", tester.test_create_task),
        ("Get All Tasks", tester.test_get_tasks),
        ("Get Single Task", tester.test_get_single_task),
        ("Update Task", tester.test_update_task),
        ("Filter by Status", tester.test_filter_tasks_by_status),
        ("Filter by Priority", tester.test_filter_tasks_by_priority),
        ("Search Tasks", tester.test_search_tasks),
        ("Delete Task", tester.test_delete_task),
        ("Unauthorized Access", tester.test_unauthorized_access)
    ]
    
    failed_tests = []
    
    for test_name, test_func in tests:
        try:
            if not test_func():
                failed_tests.append(test_name)
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {str(e)}")
            failed_tests.append(test_name)
    
    # Print final results
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS")
    print("=" * 50)
    print(f"Tests Run: {tester.tests_run}")
    print(f"Tests Passed: {tester.tests_passed}")
    print(f"Tests Failed: {len(failed_tests)}")
    
    if failed_tests:
        print(f"\n❌ Failed Tests:")
        for test in failed_tests:
            print(f"   - {test}")
    else:
        print(f"\n✅ All tests passed!")
    
    success_rate = (tester.tests_passed / tester.tests_run) * 100 if tester.tests_run > 0 else 0
    print(f"\nSuccess Rate: {success_rate:.1f}%")
    
    return 0 if len(failed_tests) == 0 else 1

if __name__ == "__main__":
    sys.exit(main())