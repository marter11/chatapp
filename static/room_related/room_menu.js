
// Send recorded values inside the modal
function SocketHandeling(data) {
  var socket = io.connect("http://"+document.domain+":"+location.port);
  socket.emit("create_room", data);
}

// Listener functions
function SetDisplay() {
  document.getElementsByClassName("modal")[0].style.display = "none";
}

function SetValues() {
  let name = document.getElementById("room_name");
  let topic = document.getElementById("room_topic");
  let password = document.getElementById("room_password");
  let capacity = document.getElementById("room_capacity");

  var data = {name: name.value, topic: topic.value, password: password.value, capacity: capacity.value};
  name.value = null;
  topic.value = null;
  password.value = null;

  SocketHandeling(data);
  document.getElementById("exit").click();
}

function ClicketRoomCreateButton() {
  let modal = document.getElementsByClassName("modal")[0];
  modal.style.display = "block";
}

// Start listen the target location
window.addEventListener('DOMContentLoaded', () => {
  document.getElementById("create_room").addEventListener("click", ClicketRoomCreateButton);

  // Hide modal board when click on X
  document.getElementById("exit").addEventListener("click", SetDisplay);

  // When finalize room creating
  document.getElementById("finalize").addEventListener("click", SetValues);


  // Catch update room signal and set among the others
  var socket = io.connect("http://"+document.domain+":"+location.port);

  socket.on("update_room_list", (data) => {
    if(data) {
      var room_location = document.getElementsByClassName("room-container")[0];
      let child = document.createElement("div");
      child.innerHTML = "<h5>"+data.name+"</h5>";
      room_location.appendChild(child);
    }
  });
});
