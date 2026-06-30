import { useEffect, useState } from "react";
import {
  Typography,
  Paper,
  Grid,
  CircularProgress,
  Box,
} from "@mui/material";

import api from "../services/api";
import MainLayout from "../layouts/MainLayout";

function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = async () => {
    try {
      const response = await api.get("/users/me");
      setUser(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!user) {
    return (
      <Box
        sx={{
          height: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  return (
    <MainLayout>
      <Typography
        variant="h3"
        color="white"
        gutterBottom
      >
        Welcome, {user.full_name} 👋
      </Typography>

      <Grid container spacing={3} mt={1}>
        <Grid item xs={12} md={6} lg={3}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">🎯 Goal</Typography>
            <Typography>{user.fitness_goal}</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6} lg={3}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">⚖ Weight</Typography>
            <Typography>{user.weight} kg</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6} lg={3}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">📏 Height</Typography>
            <Typography>{user.height} cm</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6} lg={3}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">📧 Email</Typography>
            <Typography>{user.email}</Typography>
          </Paper>
        </Grid>
      </Grid>
    </MainLayout>
  );
}

export default Dashboard;