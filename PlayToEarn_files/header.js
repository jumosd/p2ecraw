function randomString(length, chars) {
    var result = '';
    for (var i = length; i > 0; --i) result += chars[Math.round(Math.random() * (chars.length - 1))];
    return result;
}
var coinzilla_id_session_header = randomString(1,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+randomString(32, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');
var coinzilla_header = (function() {
    var coinzilla_header = {
        push: function(_coinzilla_header_id_){
            var args = {};
            if(_coinzilla_header_id_[0] === undefined) {
                _coinzilla_header_id_[0] = null;
                return;
            }
            args['z'] = _coinzilla_header_id_[0];

            if(!util.isCookieEnabled()) return;
            if(util.getCookie("_coinzilla_header_id_disabled_")) return;
            var nounce = Math.floor(Math.random()*1000000000000);
            var urlCheck = 'https://request-global.czilladx.com/serve/header.php?withoutAdCode=1&z='+args['z']+'&n='+nounce;
            var xhr = new XMLHttpRequest();
            xhr.open('GET', urlCheck);
            xhr.withCredentials = true;
            xhr.onload = function() {
                if (xhr.status === 200) {
                    var response = xhr.responseText;
                    var elem = document.querySelector(".header-"+args['z']);
                    if(typeof elem === 'undefined') {
                        return;
                    }
                    if(!elem) {
                        return;
                    }
                    elem.setAttribute("id", coinzilla_id_session_header);
                    elem.style = "width: 100%;height: 90px; position: relative; z-index: 99!important;";

                    elem = document.createElement('a');
                    elem.id = "CloseCoinzillaHeader";
                    elem.setAttribute('href','#');
                    elem.innerHTML = '<img src="https://coinzillatag.com/lib/img/close.png" style="width: 14px; height:14px;">';
                    elem.style = "line-height: 0; top: 0;left: 0;padding: 2px;text-decoration:none;font-size: 14px;background: rgba(255, 255, 255, 1);position: absolute;z-index: 999999 !important;color: rgba(0, 0, 0, .6);font-weight: 600;border-radius:0;font-family: Arial;";
                    document.getElementById(coinzilla_id_session_header).appendChild(elem);
                    args['url'] = response;
                    if(util.isEmptyString(response)) return;
                    load[args['z']] = function (args) {
                        return new this(args);
                    };
                    load[args['z']](args);
                }
            };
            xhr.send();
        }
    };
    var fullAgent = navigator.userAgent,
        userAgent = navigator.userAgent.toLowerCase(),
        mobile = {
            true: /iphone|ipad|android|ucbrowser|iemobile|ipod|blackberry|bada/.test(userAgent)
        },
        util = {
            bind: function(fn,action,target){
                if (target.addEventListener) {
                    target.addEventListener(action, fn);
                } else if (target.attachEvent) {
                    target.attachEvent("on"+action, fn);
                }
            },
            getCookie: function(name) {
                var cookieMatch = document.cookie.match(new RegExp(name + '=([^;]+)'));
                if(cookieMatch) {
                    return decodeURIComponent(cookieMatch[1]);
                }else return null;
            },
            setCookie: function(name, value, minutes, path) {
                if (minutes === null || typeof minutes == 'undefined') {
                    minutes = null;
                } else {
                    var date;
                    if (typeof minutes == 'number') {
                        date = new Date();
                        date.setTime(date.getTime() + minutes * 60 * 1e3);
                    } else {
                        date = minutes;
                    }
                    minutes = '; expires=' + date.toUTCString();
                }
                document.cookie = name + '=' + encodeURIComponent(value) + minutes + '; path=' + (path || '/');
            },
            isCookieEnabled: function(){
                return navigator.cookieEnabled;
            },
            isEmptyString : function (string) {
                return (
                    (typeof string == 'undefined')
                    ||
                    (string == null)
                    ||
                    (string == false)  //same as: !x
                    ||
                    (string.length == 0)
                    ||
                    (string == "")
                    ||
                    (string.replace(/\s/g,"") == "")
                    ||
                    (!/[^\s]/.test(string))
                    ||
                    (/^\s*$/.test(string))
                );
            }
        },
        load = function (needle) {
            this.construct(needle)
        };
    load.prototype = {
        construct: function(needle){

            this.data = needle;
            var zoneId = this.data["z"];
            var src = this.data["url"];
            var ifrm = document.createElement("iframe");
            ifrm.setAttribute("src", src);
            ifrm.setAttribute("scrolling", "no");
            ifrm.style.cssText = 'margin:0 auto; min-height: 50px;width: 100%;max-width: 100%;max-height: 90px;height: 90px;';
            ifrm.frameBorder = 0;
            ifrm.setAttribute('allowtransparency', 'true');
            ifrm.setAttribute('sandbox', 'allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation');
            ifrm.id = 'zone-'+zoneId;
            document.getElementById(coinzilla_id_session_header).appendChild(ifrm);

            util.bind(function(e){
                e.preventDefault();
                var div = document.getElementById(coinzilla_id_session_header);
                div.remove(div.selectedIndex);
                util.setCookie("_coinzilla_header_id_disabled_","true",5,"/");
            },"click",document.getElementById("CloseCoinzillaHeader"));
        }
    };
    if(typeof window.coinzilla_header !== "undefined"){
        for(var i=0; i<window.coinzilla_header.length;i++){
            coinzilla_header.push(window.coinzilla_header[i]);
        }
    }
    return coinzilla_header;
})();