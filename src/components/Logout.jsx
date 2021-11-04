import { useHistory } from "react-router";
import Cookies from "universal-cookie";

export default function Logout() {
    const cookies = new Cookies();
    let hist = useHistory();
    if (cookies.get("token")) {
        cookies.remove("token");
        window.location.reload();
        hist.push("/")
    }
    else {
        hist.push("/")
    }
    return null
}