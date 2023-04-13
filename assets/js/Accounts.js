const passwordInputs = document.querySelectorAll('.password-input');
const passwordToggles = document.querySelectorAll('.password-toggle');

passwordToggles.forEach(function(toggle, index) {
  toggle.addEventListener('click', function() {
    console.log(passwordInputs[index])
    const passwordInput = passwordInputs[index];
    if (passwordInput.type === 'password') {
      passwordInput.type = 'text';
      toggle.innerHTML = '<i class="fa fa-eye-slash" style="font-size: 18px;"></i>';
    } else {
      passwordInput.type = 'password';
      toggle.innerHTML = '<i class="fa fa-eye" style="font-size: 18px;"></i>';
    }
  });
});
