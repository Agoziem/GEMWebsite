mapboxgl.accessToken = 'pk.eyJ1Ijoib2tmcyIsImEiOiJjbDFodTNjMG8wNnh6M2tycHN0ZDhzamYzIn0.H1VgtMiBAjkMEe7GXREzvA';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-79.347015,43.651070],
  // 6.800465, 6.124938
  // 56.1304° N, 106.3468° W
  zoom: 12,
});


// Check if the user is anonymous (you can modify this condition based on your authentication system)
if (user === 'AnonymousUser') {
  // Set the time delay for showing the modal (10 minutes = 600000 milliseconds)
  const timeDelay = 20000;

  // Function to show the modal
  const showModal = () => {
    // Select the modal element by its ID
    const modal = document.getElementById('LoginModal');
  
    // Create a Bootstrap Modal instance
    const modalInstance = new bootstrap.Modal(modal);
  
    // Show the modal
    modalInstance.show();
  };

  // Set a timeout to trigger the modal after the time delay
  setTimeout(showModal, timeDelay);
}


document.getElementById('contact-form').addEventListener('submit', function(e) {
  e.preventDefault();
  var form = this;
  var btn = form.querySelector('#submit-btn');

  // Change button text to spinner icon
  btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> submitting...';
  var userformdata = {
          'name': form.Name.value,
          'email': form.email.value,
          'message': form.message.value,
        }
  // Send Ajax request
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/submit_contact_form/' );
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('X-CSRFToken', csrftoken);
  xhr.onload = function() {
    if (xhr.status === 200) {
      // Change button text back to original
      btn.innerHTML = 'Send Message';

      // Display success alert
      var successAlert = document.querySelector('.alert-success');
      successAlert.style.display = 'flex';
      setTimeout(function() {
        successAlert.style.display = 'none';
      }, 3000);
      form.reset();
      
    } else {
      // Change button text back to original
      btn.innerHTML = 'Send Message';

      // Display error alert
      var errorAlert = document.querySelector('.alert-danger');
      errorAlert.style.display = 'flex';
      setTimeout(function() {
        errorAlert.style.display = 'none';
      }, 3000);
    }
  };
  xhr.send(JSON.stringify({ userformdata: userformdata }));
});
