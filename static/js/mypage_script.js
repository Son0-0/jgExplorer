var titleinput = document.querySelector("#inputTitle");
var contentinput = document.querySelector("#inputText");
var submitBtn = document.querySelector("#submit_btn");

titleinput.addEventListener('keyup', listener);
contentinput.addEventListener('keyup', listener);

function listener() {
  switch(!(titleinput.value && contentinput.value)) {
    case true: submitBtn.disabled = true; break;
    case false: submitBtn.disabled = false; break;
  }
}