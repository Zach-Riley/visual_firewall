var app = angular.module("visualFirewallApp", [
    'ui.router'
]).config([
    '$controllerProvider', function($controllerProvider) {
        $controllerProvider.allowGlobals();
    }
]).config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/Intro');

    $stateProvider
        .state('Intro', {
            url: '/Intro',
            templateUrl: 'visualFirewallIntro.html',
            controller: 'visualFirewallIntroController'
        })
        .state('visualFirewall', {
            url: '/visualFirewall',
            templateUrl: '/visualFirewall.html',
            controller: 'visualFirewallController'
        });
});

app.factory('firewallVM', function() {

    var speed = null;
    var whiteList = [];

    var firewallVM = {};

    firewallVM.setSpeed = function(inputSpeed) {
        speed = inputSpeed;
    }
    firewallVM.addIpToWhitelist = function(whitelistIP) {
        whiteList.push(whitelistIP);
    }
    firewallVM.getWhitelist = function() {
        return whiteList;
    }
    firewallVM.getSpeed = function() {
        return speed;
    }

    return firewallVM;

});
