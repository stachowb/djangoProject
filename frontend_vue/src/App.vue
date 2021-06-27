<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Django</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to="/test1" class="navbar-item">Test1</router-link>
          <router-link to="/test2" class="navbar-item">Test2</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light">Login</router-link>
              <router-link to="/register" class="button is-success">Register</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <router-view/>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>
