import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { toast } from "sonner";
import { UserPlus } from "lucide-react";

const Register = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      await register(name, email, password);
      toast.success("Registration successful!");
      navigate("/dashboard");
    } catch (error) {
      toast.error(error.response?.data?.detail || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex">
      <div 
        className="hidden lg:block lg:w-1/2 bg-cover bg-center relative"
        style={{
          backgroundImage: "url('https://images.unsplash.com/photo-1771462883475-1c70a09cdf91?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwzfHxtaW5pbWFsaXN0JTIwYWJzdHJhY3QlMjBnZW9tZXRyaWMlMjBhcmNoaXRlY3R1cmUlMjB3aGl0ZSUyMGNvbmNyZXRlfGVufDB8fHx8MTc3MjY1NzkzN3ww&ixlib=rb-4.1.0&q=85')"
        }}
      >
        <div className="absolute inset-0 bg-white/50"></div>
      </div>
      
      <div className="w-full lg:w-1/2 flex items-center justify-center p-8">
        <div className="w-full max-w-md space-y-8">
          <div className="space-y-2">
            <h1 className="text-4xl md:text-5xl font-bold tracking-tight leading-none">Create Account</h1>
            <p className="text-base leading-relaxed text-muted-foreground">Join TaskFlow Executive today</p>
          </div>
          
          <form onSubmit={handleSubmit} className="space-y-6" data-testid="register-form">
            <div className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="name" className="text-xs uppercase tracking-widest font-bold text-muted-foreground">Full Name</Label>
                <Input
                  id="name"
                  type="text"
                  data-testid="register-name-input"
                  placeholder="John Doe"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                  className="h-11 rounded-none border-0 border-b border-input bg-transparent px-0 py-2 text-sm focus-visible:border-accent focus-visible:ring-0"
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="email" className="text-xs uppercase tracking-widest font-bold text-muted-foreground">Email</Label>
                <Input
                  id="email"
                  type="email"
                  data-testid="register-email-input"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="h-11 rounded-none border-0 border-b border-input bg-transparent px-0 py-2 text-sm focus-visible:border-accent focus-visible:ring-0"
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="password" className="text-xs uppercase tracking-widest font-bold text-muted-foreground">Password</Label>
                <Input
                  id="password"
                  type="password"
                  data-testid="register-password-input"
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  minLength={6}
                  className="h-11 rounded-none border-0 border-b border-input bg-transparent px-0 py-2 text-sm focus-visible:border-accent focus-visible:ring-0"
                />
              </div>
            </div>
            
            <Button
              type="submit"
              data-testid="register-submit-button"
              disabled={loading}
              className="w-full bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-6 rounded-sm font-medium active:scale-95"
            >
              {loading ? "Creating account..." : "Create Account"}
              {!loading && <UserPlus className="ml-2 h-4 w-4" />}
            </Button>
          </form>
          
          <p className="text-center text-sm text-muted-foreground">
            Already have an account?{" "}
            <Link to="/login" className="text-accent hover:underline font-medium" data-testid="login-link">
              Sign in
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Register;