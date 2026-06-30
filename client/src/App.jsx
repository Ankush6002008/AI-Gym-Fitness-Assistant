import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Workouts from "./pages/Workouts/Workouts";
import Diet from "./pages/Diet/Diet";
import Progress from "./pages/Progress/Progress";
import AICoach from "./pages/AICoach";
import Settings from "./pages/Settings/Settings";
import AIWorkoutGenerator from "./pages/Workouts/AIWorkoutGenerator";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/ai-workout"
          element={<AIWorkoutGenerator />}
        />

        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/diet" element={<Diet />} />
        <Route path="/progress" element={<Progress />} />
        <Route path="/ai-coach" element={<AICoach />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;