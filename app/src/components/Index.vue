<template>
    <div>
        <Header />
        <b-container>
            <b-row></b-row>
            <b-row class="centro">
                <h2>Venha comprar conosco!</h2>
                <img src="http://apasshow.com.br/blog/wp-content/uploads/2018/05/Depositphotos_7883907_l-2015.jpg" alt="">
            </b-row>
            <b-row></b-row>
        </b-container>
    </div>  
</template>
 
<script>
import Header from './Header'
export default {
 name: "Index",
 components: {Header}
};
</script>

<style>
.centro{
    display: flex;
    justify-content: center; 
}
img{
    max-width: 100%;
    max-height: 600px;
}
</style>
