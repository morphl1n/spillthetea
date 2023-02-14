function togglePass(elementClass) {
    let x = document.querySelector(`.${elementClass}`);
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }




document.addEventListener("DOMContentLoaded", () => {
    let showPass = document.querySelector('.reg-show-pass');
    showPass.addEventListener("click", () => {
        togglePass("reg-password");
        if (showPass.innerHTML == "Show"){
            showPass.innerHTML = "Hide";
        }else if( showPass.innerHTML == "Hide"){
            showPass.innerHTML = "Show";
        };
    });

    let showConfPass = document.querySelector('.reg-show-conf-pass');
    showConfPass.addEventListener("click", () => {
        togglePass("reg-pass-conf");
        if (showConfPass.innerHTML == "Show"){
            showConfPass.innerHTML = "Hide";
        }else if( showConfPass.innerHTML == "Hide"){
            showConfPass.innerHTML = "Show";
        };
    });


});


