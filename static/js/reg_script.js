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

var overlap_btn = document.querySelector("#overlap_btn");
var idinput = document.querySelector("#uidinput");

idinput.addEventListener('keyup', listener2);

function listener2() {
  switch(!(idinput.value)) {
    case true: overlap_btn.disabled = true; break;
    case false: overlap_btn.disabled = false; break;
  }
}