window.addEventListener("pywebviewready", async function () {
    const msg = await window.pywebview.api.hello();
    console.log(msg)
})