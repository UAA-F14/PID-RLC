s = tf('s');
H = 5e12/(s^3 + 20811*s^2 + 1.079e9*s + 5e12);
% --- Manual tuning ---
Kp = 1.5;
Ti = 95.6e-6;
Td = 23.9e-6;
Ki = Kp/Ti; % = 1.569e4 (consistent with Ti)
Kd = Kp*Td; % = 3.585e-5 (consistent with Td)
C_manual = pid(Kp, Ki, Kd);
% --- pidtune ---
C_auto = pidtune(H, 'PID'); % default: automatic crossover and 60° PM
% Optional: force a specific bandwidth or phase margin
% opts = pidtuneOptions('PhaseMargin', 60);
% wc = 2e5; % rad/s, choose based on your plant
% C_auto = pidtune(H, 'PID', wc, opts);
% --- Closed loops ---
T_manual = feedback(H*C_manual, 1);
T_auto = feedback(H*C_auto, 1);
% --- Plots ---
figure; step(H, T_manual, T_auto);
legend('Open loop H', 'Manual PID', 'pidtune PID'); grid on;
figure; bode(H*C_manual, H*C_auto); grid on;
legend('Manual', 'pidtune');
% --- Metrics ---
disp('Manual:'); disp(stepinfo(T_manual));
disp('pidtune:'); disp(stepinfo(T_auto));
disp(C_manual); disp(C_auto);
[Gm1,Pm1,~,Wc1] = margin(H*C_manual);
[Gm2,Pm2,~,Wc2] = margin(H*C_auto);
fprintf('Manual : PM = %.1f deg, Wc = %.3g rad/s\n', Pm1, Wc1);
fprintf('pidtune: PM = %.1f deg, Wc = %.3g rad/s\n', Pm2, Wc2);11:44 AM