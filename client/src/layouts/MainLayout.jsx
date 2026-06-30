import { Box } from "@mui/material";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

const drawerWidth = 240;

function MainLayout({ children }) {
  return (
    <>
      <Navbar />
      <Sidebar />

      <Box
        sx={{
          ml: `${drawerWidth}px`,
          mt: "64px",
          minHeight: "100vh",
          bgcolor: "#0F172A",
          p: 4,
        }}
      >
        {children}
      </Box>
    </>
  );
}

export default MainLayout;