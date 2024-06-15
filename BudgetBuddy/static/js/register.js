const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid-feedback");

usernameField.addEventListener("keyup", (e) => {
    console.log('77777',77777);

    const usernameVal = e.target.value;

    // to prevent the error message display initially
    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display='none'; // to display incase username-error

    // console.log('usernameVal', usernameVal); -> testing
    if(usernameVal.length > 0){
        fetch("/authentication/validate-username",{
            body:JSON.stringify({username: usernameVal }),
            method: "POST",
        }).then(res=>res.json())
        .then(data=>{
            console.log("data", data);
            if(data.username_error){
                usernameField.classList.add("is-invalid");
                feedBackArea.style.display='block'; // to display incase username-error
                feedBackArea.innerHTML = `<p>${data.username_error}<p>`
            }
        });
    } 
});