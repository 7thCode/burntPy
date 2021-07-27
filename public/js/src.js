Vue.component('price', {
    data: function () {
        return {
            items: [],
            selected: 'data-a',
            options: [
                { text: '価格A', value: 'data-a' },
                { text: '価格B', value: 'data-b' },
                { text: '価格C', value: 'data-c' }
            ]
        }
    },
    mounted: function ()  {
        this.load();
    },
    methods: {
        load: function () {
            var self = this;
            axios
                .get(this.selected)
                .then(function (res) {
                    self.items = res.data;
                });
        }
    },
    template: `<div class="container">
        <div class="card" style="width:fit-content;margin:16px;padding:24px;">
            <div class="col">
                <form style="margin:12px;">
                    <select class="form-select" v-model="selected" v-on:change="load">
                        <option v-for="option in options" v-bind:value="option.value">
                            {{ option.text }}
                        </option>
                    </select>
                </form>
                <ul class="list-group"  style="margin:12px;">
                    <li class="list-group" v-for="item in items">
                        {{ item.title }} : {{ item.price }}
                    </li>
                </li>
            </div>
        </div>
    </div>`
});
