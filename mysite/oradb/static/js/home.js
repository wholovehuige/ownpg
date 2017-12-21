new Vue({
    el:'#allData',
    data:{
        data:'allData'
    },
    method(){
        this.getAllData()
    },
    method:{
        getAllData:function () {
            $.ajax({
                type:'GET',
                url:'jsondata',
                cache:false,
                success:function (data) {
                    console.log(data)
                    // ve.allData = data;
                }
            })
        }
    }
})