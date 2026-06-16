import { useEffect, useState } from "react";
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css"; 


function App() {
  const [riskData, setRiskData] = useState([]);
  useEffect(() => {
    const viewer = new Cesium.Viewer("cesiumContainer", {
  infoBox: true,
  selectionIndicator: true,
});

    fetch("http://127.0.0.1:8000/visualization")
      .then((response) => response.json())
      .then((data) => {
        const iss = data.iss.current_position;
        console.log(data.debris);
        setRiskData(data.debris);
        const trail = data.iss.orbit_trail;
        const orbitPositions = [];
        trail.forEach((point) => {
  orbitPositions.push(
    Cesium.Cartesian3.fromDegrees(
      point.longitude,
      point.latitude,
      point.altitude_km * 1000
    )
  );
});

    data.debris.forEach((debrisObj) => {

  let debrisColor = Cesium.Color.LIME;

  if (debrisObj.status === "red") {
    debrisColor = Cesium.Color.RED;
  }
  else if (debrisObj.status === "yellow") {
    debrisColor = Cesium.Color.YELLOW;
  }

  viewer.entities.add({
    position: Cesium.Cartesian3.fromDegrees(
      debrisObj.current_position.longitude,
      debrisObj.current_position.latitude,
      debrisObj.current_position.altitude_km * 1000
    ),

    point: {
      pixelSize: 8,
      color: debrisColor,
    },

    description: `
      <h3>Debris ${debrisObj.catnr}</h3>
      <p><b>Status:</b> ${debrisObj.status}</p>
      <p><b>Min Distance:</b> ${debrisObj.min_distance_km} km</p>
      <p><b>Altitude:</b> ${debrisObj.current_position.altitude_km.toFixed(2)} km</p>
    `,
  });

});
        viewer.entities.add({
          position: Cesium.Cartesian3.fromDegrees(
            iss.longitude,
            iss.latitude,
            iss.altitude_km * 1000
          ),
          point: {
            pixelSize: 12,
            color: Cesium.Color.BLACK,
          },
        });
        viewer.entities.add({
  polyline: {
    positions: orbitPositions,
    width: 3,
    material: Cesium.Color.BLACK,
    arcType: Cesium.ArcType.GEODESIC,
  },
});
      
        
      });

    return () => {
      if (!viewer.isDestroyed()) {
        viewer.destroy();
      }
    };
  }, []);

  return (
  <div
    style={{
      display: "flex",
      height: "100vh",
    }}
  >
    <div
      id="cesiumContainer"
      style={{
        width: "70%",
        height: "100%",
      }}
    ></div>
<div
  style={{
    width: "30%",
    backgroundColor: "#1e293b",
    color: "white",
    padding: "20px",
    overflowY: "auto",
  }}
>
  <h2 style={{ marginBottom: "20px" }}>SSA Dashboard</h2>

  <table
    style={{
      width: "100%",
      borderCollapse: "collapse",
      fontSize: "14px",
    }}
  >
    <thead>
      <tr>
        <th
          style={{
            borderBottom: "1px solid white",
            padding: "8px",
            textAlign: "left",
          }}
        >
          CATNR
        </th>

        <th
          style={{
            borderBottom: "1px solid white",
            padding: "8px",
            textAlign: "left",
          }}
        >
          Distance
        </th>

        <th
          style={{
            borderBottom: "1px solid white",
            padding: "8px",
            textAlign: "left",
          }}
        >
          Status
        </th>
      </tr>
    </thead>

    <tbody>
      {[...riskData]
        .sort((a, b) => a.min_distance_km - b.min_distance_km)
        .map((item) => (
          <tr key={item.catnr}>
            <td style={{ padding: "8px" }}>{item.catnr}</td>

            <td style={{ padding: "8px" }}>
              {item.min_distance_km.toFixed(2)}
            </td>

            <td
              style={{
                padding: "8px",
                color:
                  item.status === "red"
                    ? "red"
                    : item.status === "yellow"
                    ? "gold"
                    : "lime",
                fontWeight: "bold",
              }}
            >
              {item.status.toUpperCase()}
            </td>
          </tr>
        ))}
    </tbody>
  </table>
</div>
  </div>
);
}

export default App;