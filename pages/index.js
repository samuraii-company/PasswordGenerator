import MainComponents from "../components/MainComponents"
import Head from "next/head"
const index = () => {
  return (
    <>
      <Head>
        <title>Open Source Password Generator</title>
        <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests" />
      </Head>
      <MainComponents />
    </>
  )
}

export default index