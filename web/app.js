// JS for real-time data handling
const client = mqtt.connect("wss://broker.hive.com:8884/mqtt");
const spotContainer = document.getElementById("spot-container");
const spots = {};

client.on("connect", function () {
  console.log("[MQTT] Connected");
  client.subscribe("parking/+/occupancy");
});

client.on("message", function (topic, message) {
  const data = JSON.parse(message.toString());
  updateSpot(data);
});

function updateSpot(data) {
  const id = data.spot_id;
  let div = spots[id];

  if (!div) {
    div = document.createElement("div");
    div.className = "spot";
    div.id = id;
    spotContainer.appendChild(div);
    spots[id] = div;
  }

  const occupied = data.is_occupied;
  const vehicle = data.vehicle_id || "None";
  const now = new Date().toLocaleTimeString();

  div.className = `spot ${occupied ? "occupied" : "available"}`;
  div.innerHTML = `
    <h3>${id}</h3>
    <p>Vehicle: ${vehicle}</p>
    <p>Status: ${occupied ? "Occupied" : "Available"}</p>
    <p>Updated: ${now}</p>
  `;
}

// Emergency exit button
function triggerEmergency() {
  fetch("http://localhost:5000/emergency-exit", { method: "POST" })
    .then((res) => res.text())
    .then(alert);
}

function controlGate() {
  const id = prompt("Enter Gate ID to control:");
  if (id) {
    fetch(`http://localhost:5000/gate/${id}`, { method: "POST" })
      .then((res) => res.text())
      .then(alert);
  }
}

function showPaymentDetails() {
  const id = prompt("Enter Spot ID for payment details:");
  if (id) {
    fetch(`http://localhost:5000/payment/${id}`, { method: "POST" })
      .then((res) => res.json())
      .then((data) => alert(`Paid ₹${data.amount} for ${data.duration} mins`));
  }
}

function controlCamera() {
  const id = prompt("Enter Camera ID to control:");
  if (id) {
    fetch(`http://localhost:5000/camera/${id}`, { method: "POST" })
      .then((res) => res.text())
      .then((msg) => alert(`Camera: ${msg}`));
  }
}
