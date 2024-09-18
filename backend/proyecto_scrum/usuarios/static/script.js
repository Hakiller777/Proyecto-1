// static/usuarios/script.js
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que el formulario se envíe de forma tradicional

  // Aquí puedes agregar código para validar el formulario, enviar datos a un servidor, etc.

  // Mostrar un mensaje de carga (opcional)
  const submitButton = document.querySelector('button[type="submit"]');
  submitButton.disabled = true; // Desactiva el botón
  submitButton.textContent = 'Cargando...';

  // Simular la espera de la respuesta del servidor (opcional)
  setTimeout(() => {
    // Habilita el botón y actualiza el texto (opcional)
    submitButton.disabled = false;
    submitButton.textContent = 'Iniciar Sesión'; 
  }, 2000);
});
