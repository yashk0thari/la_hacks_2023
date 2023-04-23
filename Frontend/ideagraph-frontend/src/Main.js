import {
  Button,
  Grid,
  IconButton,
  ListItemButton,
  Typography,
} from "@mui/material";
import { useCallback, useEffect, useState } from "react";
import {
  Background,
  Controls,
  MiniMap,
  ReactFlow,
  addEdge,
  useEdgesState,
  useNodesState,
} from "reactflow";
import "reactflow/dist/style.css";
import { Drawer } from "@mui/material";
import dagre from "dagre";
import { useNavigate } from "react-router";
import axios from "axios";
import * as d3 from "d3";

const styles = {
  mainDiv: {
    position: "relative",
    height: "100vh",
  },
  signOutButton: {
    position: "absolute",
    top: "10px",
    right: "10px",
    zIndex: "1",
  },
  recordAudioButton: {
    position: "absolute",
    top: "10px",
    right: "10px",
    zIndex: "1",
  },
  openToolbarButton: { position: "relative", top: "10px", right: "10px" },
  drawerDiv: { margin: "32px", width: "40vw" },
  sentenceDescription: { marginTop: "24px" },
  centerChildren: {
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#f6f6f6",
  },
};

const initialNodes = [
  // { id: "1", position: { x: 0, y: 0 }, data: { label: "1" } },
  // { id: "2", position: { x: 0, y: 0 }, data: { label: "2" } },
  // { id: "3", position: { x: 0, y: 0 }, data: { label: "3" } },
  // { id: "4", position: { x: 0, y: 0 }, data: { label: "4" } },
  // { id: "5", position: { x: 0, y: 0 }, data: { label: "5" } },
];
const initialEdges = [
  // { id: "e1-2", source: "1", target: "2" },
  // { id: "e1-3", source: "1", target: "3" },
  // { id: "e1-4", source: "1", target: "4" },
  // { id: "e2-5", source: "2", target: "5" },
  // { id: "e3-5", source: "3", target: "5" },
];

function Main() {
  const navigate = useNavigate();
  const [isDrawerOpen, setDrawerOpen] = useState(false);
  const [selectedNode, setSelectedNode] = useState(-1); // just have to make sure not to assign any node id -1
  const [signOutAux, setSignOutAux] = useState(false);

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  const handleNodeClick = (event, element) => {
    console.log("Node clicked:", element.id);
    setSelectedNode(element.id);
    setDrawerOpen(true);
    // post request testing
    console.log("making post request");
    const text =
      "The temperature in Tokyo is currently 25 degrees. Celsius with a relative humidity of 70%. The population of Iceland is approximately 364,000 people as of 2021. The Mona Lisa painting was created by Leonardo da Vinci in the 16th century and is currently housed in the Louvre Museum in Paris. The highest peak in the world, Mount Everest, stands at 8,848 meters above sea level. The chemical formula for water is H2O, which consists of two hydrogen atoms and one oxygen atom. The average lifespan of a housefly is only around 30 days. The speed of light is approximately 299,792,458 meters per second in a vacuum.";
    const text1 = "I love Tokyo! it's my favourite city in the world";
    const dummyData = {
      text: "UCLA is an amazing university, I love UCLA!.",
      // text : "John",
    };
    const url = "http://localhost:8080/user_input";
    axios
      .post(url, dummyData)
      .then((response) => {
        console.log(response.data.nodes);
        setNodes(response.data.nodes);
        setEdges(response.data.edges);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    const dummyData = {
      text: "UCLA is an amazing university, I love UCLA!.",
      // text : "John",
    };
    const url = "http://localhost:8080/user_input";
    axios
      .post(url, dummyData)
      .then((response) => {
        console.log(response.data.nodes);
        setNodes(response.data.nodes);
        setEdges(response.data.edges);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const simulation = d3
    .forceSimulation(nodes)
    .force(
      "link",
      d3
        .forceLink(edges)
        .id(function (d) {
          return d.name;
        })
        .distance(200)
    )
    .force("charge", d3.forceManyBody().strength(-400))
    .force("center", d3.forceCenter(0, 0));

  useEffect(() => {
    const handleClick = (event) => {
      if (selectedNode && !event.target.closest(".react-flow__node")) {
        setDrawerOpen(false);
      }
    };
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  }, [selectedNode]);

  useEffect(() => {
    if (
      !localStorage.getItem("loggedIn") ||
      localStorage.getItem("loggedIn") === "false"
    ) {
      navigate("/");
    }
  }, []);

  useEffect(() => {
    const graph = new dagre.graphlib.Graph();

    graph.setDefaultEdgeLabel(() => ({}));
    graph.setGraph({ rankdir: "TB" });

    nodes.forEach((node) => {
      console.log(node);
      graph.setNode(node.id, { width: 100, height: 100 });
    });

    edges.forEach((edge) => {
      graph.setEdge(edge.source, edge.target);
    });

    dagre.layout(graph);

    const newNodes = nodes.map((node) => ({
      ...node,
      position: {
        x: graph.node(node.id).x * 1.1,
        y: graph.node(node.id).y * 1.1,
      },
    }));

    console.log(nodes);
    setNodes(newNodes);
    console.log(newNodes);
  }, [edges]); // empty because we want to allow the user to move nodes around

  const layout = {
    name: "dagre",
    rankDir: "TB",
    nodeDimensionsIncludeLabels: true,
    animate: true,
  };

  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileInputChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUploadButtonClick = () => {
    // Handle file upload logic here
    console.log("Selected file:", selectedFile);
  };

  function recordAndSendAudio() {
    // Access the user's microphone and start recording
    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        const mediaRecorder = new MediaRecorder(stream);
        const chunks = [];

        mediaRecorder.addEventListener("dataavailable", (event) => {
          chunks.push(event.data);
        });

        mediaRecorder.addEventListener("stop", () => {
          const blob = new Blob(chunks, { type: "audio/wav" });

          // Send the audio data in a POST request
          const formData = new FormData();
          formData.append("audio", blob);

          fetch("/api/audio", {
            method: "POST",
            body: formData,
          })
            .then((response) => {
              console.log("Audio uploaded successfully!");
            })
            .catch((error) => {
              console.error("Error uploading audio:", error);
            });
        });

        // Record for 10 seconds
        mediaRecorder.start(10000);

        setTimeout(() => {
          mediaRecorder.stop();
        }, 10000);
      })
      .catch((error) => {
        console.error("Error accessing microphone:", error);
      });
  }

  useEffect(() => {
    const handleTick = () => {
      const newNodes = nodes.map((node, i) => {
        const graphNode = nodes[i];
        return {
          ...node,
          position: {
            x: graphNode.x,
            y: graphNode.y,
          },
        };
      });

      setNodes(newNodes);
    };

    simulation.on("tick", handleTick);

    return () => {
      simulation.on("tick", null); // Remove the event listener when the component is unmounted
    };
  }, [nodes, setNodes]);

  return (
    <div style={styles.mainDiv}>
      <Drawer
        open={isDrawerOpen}
        ModalProps={{ BackdropProps: { invisible: true } }}
        style={styles.drawer}
      >
        <div style={styles.drawerDiv}>
          <Typography
            fontWeight="bold"
            style={styles.typoSpaced}
            sx={{ fontSize: "1.75rem" }}
          >
            Short representation
          </Typography>
          <Typography
            style={styles.sentenceDescription}
            sx={{ fontSize: "1rem" }}
          >
            A single-sentence description of this node will appear here. The
            sentence should be about this long.
          </Typography>
        </div>
      </Drawer>
      <Button
        variant="outlined"
        style={styles.signOutButton}
        onClick={() => {
          setSignOutAux(!signOutAux);
          localStorage.setItem("loggedIn", false);
          navigate("/");
        }}
      >
        Sign Out
      </Button>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        layout={layout}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onNodeClick={handleNodeClick}
        onPaneClick={() => {
          setSelectedNode(-1);
          setDrawerOpen(false);
          console.log("onPaneClick");
        }}
      >
        <Controls />
        <MiniMap />
        <Background variant="dots" gap={12} size={1} />
      </ReactFlow>
      {nodes.length === 0 && (
        <Grid
          container
          spacing={10}
          style={{
            display: "flex",
            justifyContent: "center",
            marginTop: "-65vh",
          }}
        >
          <IconButton
            style={{
              transform: "scale(1)",
              zIndex: "1",
            }}
          >
            <img src="mic_temp.svg"></img>
          </IconButton>
          <IconButton
            style={{
              transform: "scale()",
              zIndex: "1",
            }}
          >
            <img src="upload_temp.svg"></img>
          </IconButton>
        </Grid>
      )}
      {/* <Grid container spacing={2} justifyContent="center" alignItems="center">
        <Grid item xs={12}>
          <Typography variant="h4" align="center">
            Select a file to upload
          </Typography>
        </Grid>
        <Grid item xs={12}>
          <input id="file-input" type="file" onChange={handleFileInputChange} />
          <Button variant="contained" component="span">
            Record audio
          </Button>
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleUploadButtonClick}
            disabled={!selectedFile}
            fullWidth
          >
            Upload
          </Button>
        </Grid>
      </Grid> */}
    </div>
  );
}
export default Main;
