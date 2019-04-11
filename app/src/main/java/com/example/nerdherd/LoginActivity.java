package com.example.nerdherd;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class LoginActivity extends AppCompatActivity {

    Button login_btn;
    Button signup_btn;
    Button forgotPasswordBtn;
    EditText login_email;
    EditText login_password;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //initializing the buttons
        login_btn = findViewById(R.id.login);
        signup_btn = findViewById(R.id.signup_btn);
        forgotPasswordBtn = findViewById(R.id.forgot_password);
        login_email = findViewById(R.id.login_email_field);
        login_password = findViewById(R.id.login_password_field);

        //signup activity intent
        signup_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = LoginActivity.this;
                Class signupActivity = SignupActivity.class;
                Intent intent = new Intent(context, signupActivity);
                startActivity(intent); //transition to signup screen
            }
        });

        //login activity intent
        login_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = LoginActivity.this;
                if(accountVerification()){
                    Class mainPageActivity = MainPageActivity.class;
                    Intent intent = new Intent(context, mainPageActivity);
                    startActivity(intent); //transition to main page screen
                } else {
                    AlertDialog.Builder mismatchPasswords = new AlertDialog.Builder(context);
                    mismatchPasswords.setMessage("Invalid Email or Password");
                    mismatchPasswords.setCancelable(true);
                    mismatchPasswords.setPositiveButton("OK", null);
                    mismatchPasswords.create().show();
                }

            }
        });

        //forgot password intent
        forgotPasswordBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = LoginActivity.this;
                Class sendVerificationCodeActivity = SendVerificationCodeActivity.class;
                Intent intent = new Intent(context, sendVerificationCodeActivity);
                startActivity(intent);
            }
        });

    }


    public boolean accountVerification(){
        //TODO check if email and password are a correct match
        String email = login_btn.getText().toString();
        String password = login_password.getText().toString();
        return false;
    }
}
