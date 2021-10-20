import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { Link } from "react-router-dom";
import styles from "./SearchForUser.module.css";
export default function SearchForUser() {
    const { usr } = useParams();
    const [users, setUsers] = useState([]);
    useEffect(() => {
        axios.post(`http://localhost:8000/search/user`, {"name" : usr}).then((res) => setUsers(res.data));
    }, [])
    
    return (
        <>
            {users ?<>
                <h1>Found users: </h1>
                {users.map((user) => (
                    <>
                        
                        <h2><Link className={styles.Link}  to={`/profile/${user.id}`}>{user.firstName} {user.lastName}</Link></h2>
                    </>
                ))}</>
                :
                <h1>No users Found!</h1>
            }
        </>
    )
}