var trace = window.console.log.bind(window.console);

var dcmParam, scane, wind, object, pObject, ta, ta1
var array = [];
var aButton = []
var objectBase






function creatArrApi() {
    //создаюм обьекты отправки
    
    var o = {
        name: "creat",//имя кнопки
        help: "Создаюм план, в ответ обьект планна. типа {id:234,url:'путь к json файлу',info:'asdhjf'...}, id-иди проекта, url-путь к моделе, по умолчанию сущесествует пустой, типа: '{}'",//пояснения

        obj: {//то что посылаем через аякс на сервер, собственно тут сам запрос
            url: 'https://plan.z25945zw.beget.tech/catalog/plan/22/edit_scheme/',
            type: 'GET',
            data: {
                d: JSON.stringify({ test: 10 }),
                checked: false,
                csrfmiddlewaretoken: "xz Тут нужен ключь, который генериться под юзеров "
            },
            cache: false,
            async: false,
            success: successMy,//удачиный ответ
            error: errorMy,//не удачиный ответ
        }
    }
    array.push(o);

    var o = {
        name: "getId",//имя кнопки
        help: "Возврощает обьект плана типа: {id:234,url:'путь к j....",//пояснения

        obj: {//то что посылаем через аякс на сервер, собственно тут сам запрос
            url: 'https://plan.z25945zw.beget.tech/catalog/plan/22/edit_scheme/',
            type: 'POST',
            data: {
                d: JSON.stringify({ test: 10 }),
                checked: false,
                csrfmiddlewaretoken: "xz Тут нужен ключь, который генериться под юзеров "
            },
            cache: false,
            async: false,
            success: successMy,//удачиный ответ
            error: errorMy,//не удачиный ответ
        }
    }
    array.push(o);


    var o = {
        name: "save",//имя кнопки
        help: "По идишнику записывает json пална по ",//пояснения

        obj: {//то что посылаем через аякс на сервер, собственно тут сам запрос
            url: 'https://plan.z25945zw.beget.tech/catalog/plan/22/edit_scheme/',
            type: 'POST',
            data: {
                d: JSON.stringify({ test: 10 }),
                checked: false,
                csrfmiddlewaretoken: "xz Тут нужен ключь, который генериться под юзеров "
            },
            cache: false,
            async: false,
            success: successMy,//удачиный ответ
            error: errorMy,//не удачиный ответ
        }
    }
    array.push(o);



}







function init() {
    console.log("creatArrApi");
    dcmParam = new DCM();
    scane = new DCont(document.body);
    creatArrApi();
    initInterfes();

    openObj(array[0])
}


function successMy(e) {//удачиный ответ
    ta1.colorText1 = "#007700";
    var s = JSON.stringify(e, null, 4)
    ta1.text = s
}
function errorMy(e) {//не удачиный ответ
    trace(e)
    ta1.colorText1 = "#ff0000";
    var s = JSON.stringify(e, null, 4)
    ta1.text = s
}




function openObj(o) {
    for (var i = 0; i < aButton.length; i++) {
        aButton[i].alpha = o.name == aButton[i].obj.name ? 0.5 : 1
    }
    objectBase = o

    pObject.addObject(objectBase);
    dragObj()
}
function dragObj() {

    var s = JSON.stringify(objectBase.obj, null, 4)
    ta.text = s
}


function initInterfes() {
    wind = new DWindow(scane, 0, 0, "API")
    wind.width = 1000
    wind.height = 500
    for (var i = 0; i < array.length; i++) {
        aButton[i] = new DButton(wind.content, 2, 2 + 34 * i, array[i].name, function () {
            openObj(this.obj)
        })
        aButton[i].obj = array[i]
    }
    pObject = new DParamObject(wind.content, 106, 2, function () {
        dragObj()
    }, 1);
    pObject.tipRide = true
    pObject.arrType.push("object")
    pObject.width = 333
    pObject.arrayLabel = ["help"];

    let hh = (wind.height - 20 - 4 - 32 - 36) / 2
    var b = new DButton(wind.content, pObject.x + pObject.width + 2, 2, "Посылаем", function () {
        $.ajax(objectBase.obj)
    });
    b.width = wind.width - (pObject.x + pObject.width) - 6

    ta = new DTextArea(wind.content, pObject.x + pObject.width + 2, 36, "")
    ta.textAlign = "left";
    ta.width = wind.width - ta.x - 2
    ta.height = hh
    ta.fontSize = 12
    ta.object.style.readonly = "disabled";


    new DLabel(wind.content, pObject.x + pObject.width, 36 + hh, "Принимаем")
    ta1 = new DTextArea(wind.content, pObject.x + pObject.width, 36 + 20 + hh, "")
    ta1.width = wind.width - ta.x - 2
    ta1.height = hh;
    ta1.textAlign = "left";
    ta1.fontSize = 12
}

