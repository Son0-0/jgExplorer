var submitBtn = document.getElementById("submit_btn");
var unameinput = document.querySelector("#uidinput");
var uidinput = document.querySelector("#uidinput");
var upwinput = document.querySelector("#upwinput");

uidinput.addEventListener('keyup', listener);
upwinput.addEventListener('keyup', listener);
unameinput.addEventListener('keyup', listener);

function listener() {
  switch(!(uidinput.value && upwinput.value && unameinput.value)) {
    case true: submitBtn.disabled = true; break;
    case false: submitBtn.disabled = false; break;
  }
}