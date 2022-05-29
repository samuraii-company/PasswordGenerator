import styles from "../styles/MainComponent.module.scss"
import React from "react"
import { AiFillGithub } from "react-icons/ai"
import axios from "axios";


const MainComponents = () => {
    const [value, setValue] = React.useState(20);
    const [num, setNum] = React.useState(false);
    const [sym, setSym] = React.useState(false);
    const [password, setPassword] = React.useState("");
    const sendRequest = async () => {
        const apiUrl = `${process.env.NEXT_PUBLIC_HOST_URL}/api/v1/password/?count=${value}&numbers=${num}&symbols=${sym}`;
        await axios.get(apiUrl).then((resp) => {
            const newPassword = resp.data;
            setPassword(newPassword.password);
        });
    }
    React.useEffect(() => {
        sendRequest()
    }, [value, num, sym])


    return (
        <div className={styles.wrapper}>
            <div className={styles.container}>
                <div className={styles.text_wrapper}>
                    <h1>Generate a secure password</h1>
                    <h2>Use our online password generator to instantly create a secure, random password. </h2>
                </div>
                <div className={styles.input_box}>
                    <h1>{password}</h1>
                </div>
                <div className={styles.settings}>
                    <div className={styles.slider}>
                        <input
                            id="count"
                            type="range"
                            min="20" max="100"
                            value={value}
                            onChange={(event) => setValue(event.target.value)}
                            step="1" />
                        <h1>{value}</h1>
                    </div>
                    <div className={styles.checkbox}>
                        <input type="checkbox" id="num" onChange={() => setNum(!num)} />
                        <label htmlFor="num">Numbers</label>
                        <input type="checkbox" id="sym" onChange={() => setSym(!sym)} />
                        <label htmlFor="sym">Symbols</label>
                    </div>
                </div>
                <div className={styles.btn_wrap}>
                    <button onClick={() => sendRequest()}>Update Password</button>
                    <button onClick={() => { navigator.clipboard.writeText(password) }}>Copy Password</button>
                </div>
                <a href="https://github.com/samuraii-company/PasswordGenerator"><AiFillGithub /></a>
            </div>
        </div>
    )
}


export default MainComponents;