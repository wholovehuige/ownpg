new Vue({
    el:'#allData',
    data:{
        data:''
    },
    method(){
        this.getAllData()
    },
    method:{
        getAllData:function () {
            $.ajax({
                type:'GET',
                url:'/oradb/jsondata/',
                dataType: 'json',
                cache:false,
                success:function (data) {
                    console.log(data)
                    ve.data = data;
                }
            })
        }
    }
})