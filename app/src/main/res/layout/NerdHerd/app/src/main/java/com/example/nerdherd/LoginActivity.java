package com.example.nerdherd;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class LoginActivity extends AppCompatActivity {

    Button login;
    EditText login_password;
    EditText login_email;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //initializing components
        login = findViewById(R.id.login);
        login_password = findViewById(R.id.login_password_field);
        login_email = findViewById(R.id.login_email_field);

        //setting onclick listeners for buttons
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = LoginActivity.this;

                if (accountVerification()) {
                    //TODO login is successful so then move to the next intent
                } else {
                    //TODO display TOAST msg that either email/password is incorrect
                }
            }
        });
    }


    public static boolean accountVerification(){
        //TODO check if email and password are a correct match
        return true;
    }
}
