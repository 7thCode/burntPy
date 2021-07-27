Vue.component('expr', {
    data: function () {
        return {
            result:"",
            number: "10",
        }
    },
    mounted: function () {
        this.load();
    },
    methods: {
        load: function () {
            var self = this;
            axios.post("expr1", {num: this.number})
                .then(function (res) {
                    self.result = res.data;
                });
        }
    },
    template: `<div class="container">
        <div class="card" style="width:fit-content;margin:16px;padding:24px;">
            <div class="col">
                <form style="margin:12px;">
                    <div>
                        <label for="expr" class="form-label">Hoge</label>
                        <input id="expr" type="text" class="form-control" v-model="number">
                    </div>
                    <button v-on:click="load" type="button" class="btn btn-primary">Primary</button>
                </form>
                {{result.expr}}
            </div>
        </div>
    </div>`
});
