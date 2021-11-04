import axios from "axios";
import { useState } from "react";
import { useHistory } from "react-router";
import Cookies from 'universal-cookie';

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassowrd] = useState("");
    let hist = useHistory()
    const cookies = new Cookies();
    const success = (res) => {
        hist.push("/")
        window.location.reload();
        cookies.set('token', res.data.access_token, { path: '/' })
    }
    const login = () => {
        
        const serar = new URLSearchParams();
        serar.append('username', username);
        serar.append('password', password);
        axios.post("http://localhost:8000/token", serar.toString(), { headers: { "Content-Type": "application/x-www-form-urlencoded" } }).then((res) => success(res)).catch(function (error) {
    alert("Wrong username or passsword")
  });
        
    }
    return (
        <>
            <input type="text" name="_login_" id="login_" onChange={e => setUsername(e.target.value)}/>
            <input type="password" name="_passwd_" id="passwd_" onChange={e => setPassowrd(e.target.value)}/>
            <input type="button" value="LOGIN" onClick={login}/>
        </>
    )
    
}