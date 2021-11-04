import React, {useState} from 'react'
import axios from 'axios'
import styles from './Add.module.css'
import { useHistory } from "react-router-dom";

export default function AddPost() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [phoneNumber, setPhoneNumber] = useState("");
    const [passwd, setPasswd] = useState("");
    let hist = useHistory()
    const add = async (e) => {
        e.preventDefault()
            await axios.post("http://localhost:8000/users", { "username": username, "passwordHash": passwd, "email": email, "phoneNumber": phoneNumber }).then((res) => hist.push("/")).catch(function (error) {
    alert("This user already exists")
  });
    }
    return (
        <form className={styles.Form} onSubmit={add}>
            <label className={styles.Label} for="_username_">
                username
            </label>
                <input className={styles.Input} type="text" name="_username" id="_username_" onChange={e => setUsername(e.target.value)} />
            
            <br />
            <label className={styles.Label} for="_passwd_">
                password
            </label>
            <input className={styles.Input} type="password" name="_passwd" id="_passwd_" onChange={e => setPasswd(e.target.value)} />
            <br />
            <label className={styles.Label} for="_email_">
                email
            </label>
            <input className={styles.Input} type="email" name="_email" id="_email_" onChange={e => setEmail(e.target.value)} />
            <br />
            <label className={styles.Label} for="_phone_">
                phone number
            </label>
            <input className={styles.Input} type="text" name="_phone" id="_phone_" onChange={e => setPhoneNumber(e.target.value)} />
            <br/>
            <input className={styles.Input} type="submit" value="Register"/>
        </form>
    )
}