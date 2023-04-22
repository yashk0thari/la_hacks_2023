import { Typography } from "@mui/material";
import "./LoginScreen.css";
import { useEffect } from "react";

const styles = {
  splitScreen: {
    display: "flex",
    flexDirection: "row",
  },
  topPane: {
    marginLeft: "-8px",
    marginTop: "-8px", // i have no idea why it's making me do this
    width: "60%",
    height: "100vh",
    backgroundColor: "blue",
  },
  bottomPane: {
    width: "40%",
    height: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  whiteText: {
    textColor: "white",
  },
  typoSpaced: {
    marginTop: "32px",
    marginLeft: "32px",
  },
};

function LoginScreen() {
  function decodeJwtResponse(token) {
    var base64Url = token.split(".")[1];
    var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    var jsonPayload = decodeURIComponent(
      window
        .atob(base64)
        .split("")
        .map(function (c) {
          return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
        })
        .join("")
    );
    return JSON.parse(jsonPayload);
  }
  function handleCallbackResponse(response) {
    console.log(decodeJwtResponse(response.credential));
  }

  useEffect(() => {
    /* global google */
    google.accounts.id.initialize({
      client_id:
        "294413887319-kvn405igs680u0b3kiclo1p7q2cd6pic.apps.googleusercontent.com",
      callback: handleCallbackResponse,
    });
    google.accounts.id.renderButton(document.getElementById("signInDiv"), {
      theme: "filled_black",
      size: "large",
      shape: "pill",
      width: 250,
    });
  }, []);

  return (
    <div className="App" style={styles.splitScreen}>
      <div style={styles.topPane}>
        {/* <h1 style={styles.whiteText}>Welcome to IdeaGraph.</h1> */}
        <Typography
          style={styles.typoSpaced}
          sx={{ fontSize: "7rem", color: "white" }}
        >
          Welcome to IdeaGraph.
        </Typography>

        <Typography
          style={styles.typoSpaced}
          sx={{ fontSize: "2.5rem", color: "white" }}
        >
          An AI-powered assistant for your consciousness.
        </Typography>
      </div>
      <div style={styles.bottomPane}>
        <div id="signInDiv"></div>
      </div>
    </div>
  );
}

export default LoginScreen;
