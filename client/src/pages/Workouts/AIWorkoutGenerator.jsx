import { useState } from "react";
import {
  Box,
  Typography,
  Paper,
  TextField,
  Button,
  MenuItem,
  Grid,
  CircularProgress,
} from "@mui/material";

import MainLayout from "../../layouts/MainLayout";
import api from "../../services/api";

function AIWorkoutGenerator() {
  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    goal: "Muscle Gain",
    experience: "Beginner",
    equipment: "Gym",
    days_per_week: 5,
    workout_duration: 60,
    injuries: "",
  });

  const [workout, setWorkout] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const generateWorkout = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/ai/generate-workout",
        formData
      );

      setWorkout(response.data.workout);
    } catch (error) {
      console.error(error);
      alert("Failed to generate workout");
    } finally {
      setLoading(false);
    }
  };

  return (
    <MainLayout>
      <Typography variant="h4" color="white" mb={3}>
        ✨ AI Workout Generator
      </Typography>

      <Paper sx={{ p: 3 }}>
        <Grid container spacing={2}>
          <Grid item xs={12} md={6}>
            <TextField
              select
              fullWidth
              label="Goal"
              name="goal"
              value={formData.goal}
              onChange={handleChange}
            >
              <MenuItem value="Muscle Gain">Muscle Gain</MenuItem>
              <MenuItem value="Fat Loss">Fat Loss</MenuItem>
              <MenuItem value="Strength">Strength</MenuItem>
            </TextField>
          </Grid>

          <Grid item xs={12} md={6}>
            <TextField
              select
              fullWidth
              label="Experience"
              name="experience"
              value={formData.experience}
              onChange={handleChange}
            >
              <MenuItem value="Beginner">Beginner</MenuItem>
              <MenuItem value="Intermediate">Intermediate</MenuItem>
              <MenuItem value="Advanced">Advanced</MenuItem>
            </TextField>
          </Grid>

          <Grid item xs={12} md={6}>
            <TextField
              fullWidth
              label="Equipment"
              name="equipment"
              value={formData.equipment}
              onChange={handleChange}
            />
          </Grid>

          <Grid item xs={12} md={6}>
            <TextField
              fullWidth
              type="number"
              label="Days Per Week"
              name="days_per_week"
              value={formData.days_per_week}
              onChange={handleChange}
            />
          </Grid>

          <Grid item xs={12} md={6}>
            <TextField
              fullWidth
              type="number"
              label="Workout Duration"
              name="workout_duration"
              value={formData.workout_duration}
              onChange={handleChange}
            />
          </Grid>

          <Grid item xs={12}>
            <TextField
              fullWidth
              label="Injuries"
              name="injuries"
              value={formData.injuries}
              onChange={handleChange}
            />
          </Grid>

          <Grid item xs={12}>
            <Button
              variant="contained"
              size="large"
              onClick={generateWorkout}
            >
              Generate Workout
            </Button>
          </Grid>
        </Grid>
      </Paper>

      {loading && (
        <Box mt={4}>
          <CircularProgress />
        </Box>
      )}

      {workout && (
  <Paper sx={{ mt: 4, p: 4 }}>
    <Typography variant="h4" gutterBottom>
      {workout.plan_name}
    </Typography>

    <Typography mb={4}>
      {workout.summary}
    </Typography>

    {workout.days.map((day, index) => (
      <Paper
        key={index}
        elevation={3}
        sx={{
          p: 3,
          mb: 3,
          backgroundColor: "#f8f9fa",
        }}
      >
        <Typography variant="h5">
          📅 {day.day}
        </Typography>

        <Typography
          color="primary"
          mb={2}
        >
          {day.focus}
        </Typography>

        {day.exercises.map((exercise, i) => (
          <Paper
            key={i}
            sx={{
              p: 2,
              mb: 2,
            }}
          >
            <Typography variant="h6">
              🏋 {exercise.name}
            </Typography>

            <Typography>
              Sets: {exercise.sets}
            </Typography>

            <Typography>
              Reps: {exercise.reps}
            </Typography>

            <Typography>
              Rest: {exercise.rest_seconds} sec
            </Typography>
          </Paper>
        ))}
      </Paper>
    ))}
  </Paper>
)}
    </MainLayout>
  );
}

export default AIWorkoutGenerator; 