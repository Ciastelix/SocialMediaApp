import axios from "axios";
import { useState } from "react";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassowrd] = useState("");
    const login = () => {
        let formdata = new FormData();
        formdata.append('username', username);
        formdata.append('password', password);
        axios.post("http://localhost:8000/token/", formdata).then((res) => console.log(res));
    }
    return (
        <>
            <input type="text" name="_login_" id="login_" onChange={e => setUsername(e.target.value)}/>
            <input type="password" name="_passwd_" id="passwd_" onChange={e => setPassowrd(e.target.value)}/>
            <input type="button" value="LOGIN" onClick={login}/>
        </>
    )
    
}