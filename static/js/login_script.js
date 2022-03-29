var signinBtn = document.getElementById("signin_btn");

signinBtn.onclick = function () {
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