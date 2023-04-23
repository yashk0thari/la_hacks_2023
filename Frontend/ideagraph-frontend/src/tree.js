import * as d3 from "d3";

const graph = {
  nodes: [
    { name: "Alice" },
    { name: "Bob" },
    { name: "Chen" },
    { name: "Dawg" },
    { name: "Ethan" },
    { name: "George" },
    { name: "Frank" },
    { name: "Hanes" },
  ],
  links: [
    { source: "Alice", target: "Bob" },
    { source: "Chen", target: "Bob" },
    { source: "Dawg", target: "Chen" },
    { source: "Hanes", target: "Frank" },
    { source: "Hanes", target: "George" },
    { source: "Dawg", target: "Ethan" },
  ],
};

const simulation = d3
  .forceSimulation(graph.nodes)
  .force(
    "link",
    d3.forceLink(graph.links).id(function (d) {
      return d.name;
    })
  )
  .force("charge", d3.forceManyBody().strength(-40))
  .force("center", d3.forceCenter(0, 0))
  .stop();

// Run the simulation to get the initial positions
for (let i = 0; i < 300; ++i) {
  simulation.tick();
}

export { graph };
