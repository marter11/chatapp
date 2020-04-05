// Send recorded values inside the modal
function SocketHandeling(data) {
  var socket = io.connect("http://"+document.domain+":"+location.port);
  console.log(data);
  socket.emit("create_room", data);
}

// Get cookies and convert to python readable
function GetCookies() {
  let cookie_data = document.cookie.split("=");
  let cookie_length = cookie_data.length;
  let session = cookie_data[cookie_length-1];
  return session;
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

  data["session"] = GetCookies();
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
      child.className = "item";

      var room_options = "<i></i>";
      let session = GetCookies();
      if(session === data["session"]) {
        room_options = '<i class="fas fa-cog" onclick="ToggleRoomOptions(event)"><span class="options-popup"><span>Change</span><span>Delete</span></span></i>';
      }

      // SECURITY ISSUE: XSS vulnerability when pass this <scr\0ipt>alert("XSSed");</scr\0ipt>
      // This issue is only valid when the user creates a new room and gives arbitrary parameters
      // The given parameters should be escaped
      child.innerHTML =
        `
          <p>${data.name}</p>
          <p>${data.topic}</p>
          <p>${data.password}</p>
          <p>${data.capacity}</p>
          ${room_options}
          <button type="button" name="join">Join</button>
        `;
      room_location.appendChild(child);
    }
  });
});
