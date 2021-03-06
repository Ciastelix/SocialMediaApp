import React, {useState } from 'react'
import { Link, useHistory } from 'react-router-dom'
import styles from "./NavBar.module.css"

import Cookies from 'universal-cookie'

export default function () {
    let hist = useHistory()
    const cookies = new Cookies();
    const search = () => {
        hist.push(`/user/search/${name}`)
    } 
    const [name, setName] = useState("")
    return (
        <nav>
            <div className={styles.NavBarContainer}>
            <ul className={styles.NavBar}>
                <li className={styles.NavItem}><Link className={styles.Link} to="/"><ion-icon name="home-outline"></ion-icon> home page</Link></li>
                <li className={styles.NavItem}><Link className={styles.Link} to="/add/post"> add post</Link></li>
                <li className={styles.NavItemS}><input onChange={e => setName(e.target.value)} className={styles.Search} type="text" placeholder="Search..."/><button onClick={search} className={styles.Btn}> Search</button></li>
                </ul>
            </div>
        </nav>
    )
}