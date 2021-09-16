import React, {useState} from 'react'
import axios from 'axios'
import styles from './Add.module.css'
export default function AddPost() {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [passwd, setPasswd] = useState("");
    const add = () => {
        let formData = new FormData();
        formData.append('firstName', firstName)
        formData.append('lastName', lastName)
        axios.post("http://localhost:8000/api/add-post", formData).then((res)=>console.log(res))
    }
    return (
        <form className={styles.Form}>
            <label className={styles.Label} for="_firstName_">
                first{'\u00A0'}name
            </label>
                <input className={styles.Input} type="text" name="_firstName" id="_firstName_" onClick={e => setFirstName(e.target.value)} />
            
            <br />
            <label className={styles.Label} for="_lastName_">
                last{'\u00A0'}name
            </label>
            <input className={styles.Input} type="text" name="_lastName" id="_lastName_" onClick={e => setLastName(e.target.value)} />
            <br />
            <label className={styles.Label} for="_passwd_">
                password
            </label>
            <input className={styles.Input} type="password" name="_passwd" id="_passwd_" onClick={e => setPasswd(e.target.value)} />
            <br />
            <label className={styles.Label} for="_email_">
                email
            </label>
            <input className={styles.Input} type="email" name="_email" id="_email_" onClick={e => setEmail(e.target.value)} />
            <br/>
            <input className={styles.Input} type="button" value="Add Post" onClick={add}/>
        </form>
    )
}