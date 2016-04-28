(function() {

    angular.module('visualFirewallModule', []).configurable(function($urlRouterProvider, $stateProvider) {

        $stateProvider
            .state('Intro', {
                url: '/Intro',
                templateUrl: '/visualFirewallIntro.html',
                controller: 'visualFirewallIntroController'
            })
            .state('visualFirewall', {
                url: '/visualFirewall',
                templateUrl: '/visualFirewall.html',
                controller: 'visualFirewallController'
            });
    });


}());
