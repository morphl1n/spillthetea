function togglePass() {
    let x = document.querySelector('.password-input');
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }


document.addEventListener("DOMContentLoaded", () => {
    let show = document.querySelector('.show-pass');
    show.addEventListener("click", () => {
        togglePass();
        if (show.innerHTML == "Show"){
          show.innerHTML = "Hide";
      }else if( show.innerHTML == "Hide"){
          show.innerHTML = "Show";
      };
    });

});

