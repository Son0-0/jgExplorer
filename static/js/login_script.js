var loginBtn = document.querySelector("#login_btn");
var uidinput = document.querySelector("#uidinput");
var upwinput = document.querySelector("#upwinput");

uidinput.addEventListener('keyup', listener);
upwinput.addEventListener('keyup', listener);

function listener() {
  switch(!(uidinput.value && upwinput.value)) {
    case true: loginBtn.disabled = true; break;
    case false: loginBtn.disabled = false; break;
  }
}

loginBtn.onclick = function () {
  var signinform = document.createElement("form");
  signinform.setAttribute("method", "POST");

  var param = document.getElementsByClassName("form-control");

  for (var i = 0; i < param.length; i++) {
    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", param[i].getAttribute("name"));
    hiddenField.setAttribute("value", param[i].value);
    signinform.appendChild(hiddenField);
  }

  document.body.appendChild(signinform);
  signinform.submit();
}