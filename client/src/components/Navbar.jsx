import {
  AppBar,
  Toolbar,
  Typography,
  Avatar,
  Box,
  IconButton,
} from "@mui/material";

import FitnessCenterIcon from "@mui/icons-material/FitnessCenter";

function Navbar() {
  return (
    <AppBar
      position="fixed"
      sx={{
        bgcolor: "#1E293B",
        zIndex: (theme) => theme.zIndex.drawer + 1,
      }}
    >
      <Toolbar>
        <FitnessCenterIcon sx={{ mr: 2 }} />

        <Typography
          variant="h6"
          sx={{ flexGrow: 1, fontWeight: "bold" }}
        >
          AI Gym Assistant
        </Typography>

        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            gap: 2,
          }}
        >
          <Typography>Ankush</Typography>

          <IconButton color="inherit">
            <Avatar>A</Avatar>
          </IconButton>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;