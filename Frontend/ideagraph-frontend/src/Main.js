import { Button, ListItemButton, Typography } from "@mui/material";
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

const styles = {
  mainDiv: { position: "relative", height: "100vh" },
  signOutButton: { position: "absolute", top: "10px", right: "10px" },
  openToolbarButton: { position: "relative", top: "10px", right: "10px" },
  drawerDiv: { margin: "32px", width: "40vw" },
  sentenceDescription: { marginTop: "24px" },
};

const initialNodes = [
  { id: "1", position: { x: 0, y: 0 }, data: { label: "1" } },
  { id: "2", position: { x: 0, y: 0 }, data: { label: "2" } },
  { id: "3", position: { x: 0, y: 0 }, data: { label: "3" } },
  { id: "4", position: { x: 0, y: 0 }, data: { label: "4" } },
  { id: "5", position: { x: 0, y: 0 }, data: { label: "5" } },
];
const initialEdges = [
  { id: "e1-2", source: "1", target: "2" },
  { id: "e1-3", source: "1", target: "3" },
  { id: "e1-4", source: "1", target: "4" },
  { id: "e2-5", source: "2", target: "5" },
  { id: "e3-5", source: "3", target: "5" },
];

function Main() {
  const [isDrawerOpen, setDrawerOpen] = useState(false);
  const [selectedNode, setSelectedNode] = useState(-1); // just have to make sure not to assign any node id -1

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
  };

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
    const graph = new dagre.graphlib.Graph();

    graph.setDefaultEdgeLabel(() => ({}));
    graph.setGraph({ rankdir: "TB" });

    nodes.forEach((node) => {
      graph.setNode(node.id, { width: 100, height: 100 });
    });

    edges.forEach((edge) => {
      graph.setEdge(edge.source, edge.target);
    });

    dagre.layout(graph, {
      nodeSep: 32,
      rankSep: 32,
    });

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
  }, []); // empty because we want to allow the user to

  const layout = {
    name: "dagre",
    rankDir: "TB",
    nodeDimensionsIncludeLabels: true,
    animate: true,
  };

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
      <Button variant="outlined" style={styles.signOutButton}>
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
    </div>
  );
}
export default Main;