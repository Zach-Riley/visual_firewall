angular.module("visualFirewallApp").controller("visualFirewallController", visualFirewallController);

function visualFirewallController($scope, firewallVM) {
    var vm =
    {
        speed: null,
        whiteList: []

    };

    init();

    function init() {
        $scope.vm = vm;
        vm.speed = firewallVM.getSpeed();
        vm.whiteList = firewallVM.getWhitelist();
    }
}