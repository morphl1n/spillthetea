// we added event handler on the edit buttons in DOM
function editHandler(event){
  
    let child = event.target;

    // all the p tags are previus siblings of button in DOM
    let p = child.previousElementSibling;
    let textarea = document.createElement("textarea");
    textarea.value = p.innerHTML;
    textarea.classList.add("edit-textarea");
    textarea.rows = 3;
    textarea.cols = 30;
    // until we are in edit mode, replace p tag with textarea and add save button
    p.parentNode.replaceChild(textarea, p);

    // remove edit button
    child.style.display = "none";
    
    // add cancel button to text area
    let cancel = document.createElement("button");
    cancel.innerHTML = "Cancel";
    cancel.classList.add("edit-cancel");
    child.insertAdjacentElement("beforebegin", cancel);

    // add save button
    let save = document.createElement("button");
    save.innerHTML = "Save";
    save.classList.add("edit-save");
    child.insertAdjacentElement("beforebegin", save);

    // if pressed cancel return unchanged p tag
    cancel.addEventListener("click", () => {
        child.style.display = "block" ;
        textarea.parentNode.replaceChild(p, textarea);
        cancel.remove();
        save.remove();

    })

    save.addEventListener("click", () => {
        textareaValue = textarea.value;
        cancel.remove();
        save.remove();
        let postID = child.dataset.variable;

        // create function for csrf validation
        function getCookie(name){
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if(parts.length == 2) return parts.pop().split(';').shift();
        }
        
        fetch("/edittext", {
            method: 'POST',
            headers: {"Content-type": "application/json", "X-CSRFToken": getCookie("csrftoken")},
            body: JSON.stringify({
                textareaValue: textareaValue,
                postID: postID
            })
        })
        .then(response => response.json())
        .then(result => { 
            p.innerHTML = result.data;
            textarea.parentNode.replaceChild(p, textarea); 
            child.style.display = "block" ;

        })
    });

}


function likeHandler(event, postID){
    console.log(postID)

    let currUnlikeButton = document.querySelector(`.bttn-unlike-${postID}`);
    currUnlikeButton.style.display = "flex";
    let currLikeButton = document.querySelector(`.bttn-like-${postID}`);
    currLikeButton.style.display = "none";

    // csrf verification
    function getCookie(name){
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if(parts.length == 2) return parts.pop().split(';').shift();
    }

    //get element we are working on
    let child = event.target;

    //get postID from the function input
    let postid = postID

    fetch("/like", {
        method: 'POST',
        headers: {"Content-type": "application/json", "X-CSRFToken": getCookie("csrftoken")},
        body: JSON.stringify({
            postid: postid
        })
    })
    .then(response => response.json())
    .then(result => {
        currUnlikeButton.innerHTML = `<svg class="unlike-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g id="SVGRepo_bgCarrier" stroke-width="0"/>
        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
        <g id="SVGRepo_iconCarrier"> <path opacity="0.4" d="M18 18.86H17.24C16.44 18.86 15.68 19.17 15.12 19.73L13.41 21.42C12.63 22.19 11.36 22.19 10.58 21.42L8.87 19.73C8.31 19.17 7.54 18.86 6.75 18.86H6C4.34 18.86 3 17.53 3 15.89V4.97998C3 3.33998 4.34 2.01001 6 2.01001H18C19.66 2.01001 21 3.33998 21 4.97998V15.89C21 17.52 19.66 18.86 18 18.86Z" fill="#0a66c2"/> <path d="M16.5805 9.56998C16.3905 9.29998 16.0705 9.15 15.6905 9.15H13.7405C13.6105 9.15 13.4905 9.09998 13.4105 8.99998C13.3305 8.89998 13.2905 8.76998 13.3105 8.62998L13.5505 7.06998C13.6505 6.60998 13.3405 6.07997 12.8805 5.92997C12.4505 5.76997 11.9405 5.98995 11.7405 6.28995L9.80048 9.16996V8.80997C9.80048 8.10997 9.50047 7.81998 8.76047 7.81998H8.27048C7.53048 7.81998 7.23047 8.10997 7.23047 8.80997V13.59C7.23047 14.29 7.53048 14.58 8.27048 14.58H8.76047C9.46047 14.58 9.76047 14.31 9.79047 13.67L11.2605 14.8C11.4605 15 11.9105 15.11 12.2305 15.11H14.0805C14.7205 15.11 15.3605 14.63 15.5005 14.04L16.6705 10.48C16.8005 10.16 16.7705 9.82998 16.5805 9.56998Z" fill="#0a66c2"/> </g>
        </svg> ${result.likes}`;
        console.log(result.liked);
    })
};

function unLikeHandler(event, postID){
    let currUnlikeButton = document.querySelector(`.bttn-unlike-${postID}`);
    currUnlikeButton.style.display = "none";
    let currLikeButton = document.querySelector(`.bttn-like-${postID}`);
    currLikeButton.style.display = "flex";

    
    // csrf verification
    function getCookie(name){
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if(parts.length == 2) return parts.pop().split(';').shift();
    }

    //get element we are working on
    let child = event.target;

    //get postID from the function input
    let postid = postID

    fetch("/unlike", {
        method: 'POST',
        headers: {"Content-type": "application/json", "X-CSRFToken": getCookie("csrftoken")},
        body: JSON.stringify({
            postid: postid
        })
    })
    .then(response => response.json())
    .then(result => {
        currLikeButton.innerHTML = `<svg class="like-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path opacity="0.4" d="M18 18.86H17.24C16.44 18.86 15.68 19.17 15.12 19.73L13.41 21.42C12.63 22.19 11.36 22.19 10.58 21.42L8.87 19.73C8.31 19.17 7.54 18.86 6.75 18.86H6C4.34 18.86 3 17.53 3 15.89V4.97998C3 3.33998 4.34 2.01001 6 2.01001H18C19.66 2.01001 21 3.33998 21 4.97998V15.89C21 17.52 19.66 18.86 18 18.86Z" fill="#292D32"/>
        <path d="M16.5805 9.56998C16.3905 9.29998 16.0705 9.15 15.6905 9.15H13.7405C13.6105 9.15 13.4905 9.09998 13.4105 8.99998C13.3305 8.89998 13.2905 8.76998 13.3105 8.62998L13.5505 7.06998C13.6505 6.60998 13.3405 6.07997 12.8805 5.92997C12.4505 5.76997 11.9405 5.98995 11.7405 6.28995L9.80048 9.16996V8.80997C9.80048 8.10997 9.50047 7.81998 8.76047 7.81998H8.27048C7.53048 7.81998 7.23047 8.10997 7.23047 8.80997V13.59C7.23047 14.29 7.53048 14.58 8.27048 14.58H8.76047C9.46047 14.58 9.76047 14.31 9.79047 13.67L11.2605 14.8C11.4605 15 11.9105 15.11 12.2305 15.11H14.0805C14.7205 15.11 15.3605 14.63 15.5005 14.04L16.6705 10.48C16.8005 10.16 16.7705 9.82998 16.5805 9.56998Z" fill="#292D32"/>
        </svg> ${result.likes}`;
        console.log(result.message);
    })
};





